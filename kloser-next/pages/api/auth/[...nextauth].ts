import axios from 'axios';
import NextAuth from 'next-auth';
import Credentials from 'next-auth/providers/credentials';
import GoogleProvider from 'next-auth/providers/google';

const CLIENT_ID = process.env.NEXT_PUBLIC_GOOGLE_CLIENT_ID;
console.log('CLIENT_ID', CLIENT_ID);
const CLIENT_SECRET = process.env.NEXT_PUBLIC_GOOGLE_CLIENT_SECRET;
console.log('CLIENT_SECRET', CLIENT_SECRET);

const providers = [
  GoogleProvider({
    clientId: CLIENT_ID,
    clientSecret: CLIENT_SECRET,
  }),
  Credentials({
    // The name to display on the sign in form (e.g. 'Sign in with...')
    name: 'Credentials',
    // The credentials is used to generate a suitable form on the sign in page.
    // You can specify whatever fields you are expecting to be submitted.
    // e.g. domain, username, password, 2FA token, etc.
    credentials: {
      username: { label: 'Username', type: 'text', placeholder: 'jsmith' },
      password: { label: 'Password', type: 'password' },
    },
    authorize: async (credentials) => {
      // Add logic here to look up the user from the credentials supplied
      const user = { id: 1, name: 'J Smith', email: 'jsmith@example.com' };

      if (user) {
        // call your DRF sign in endpoint here
        // Any object returned will be saved in `user` property of the JWT
        return Promise.resolve(user);
      } else {
        // If you return null or false then the credentials will be rejected
        return Promise.resolve(null);
        // You can also Reject this callback with an Error or with a URL:
        // return Promise.reject(new Error('error message')) // Redirect to error page
        // return Promise.reject('/path/to/redirect')        // Redirect to a URL
      }
    },
  }),
];

interface Callbacks {
  signIn?: Function;
  jwt?: Function;
  session?: Function;
}

const callbacks: Callbacks = {};

async function getTokenFromAPI(type: string, user: any) {
  try {
    const response = await axios.post(
      `${process.env.NEXT_PUBLIC_API_URL}/api/auth`
    );
    console.log('response', response);
    return response;
  } catch (error) {
    console.error('error', error);
  }
}

callbacks.signIn = async function signIn(
  user: any,
  account: any,
  metadata: any
) {
  if (account.provider === 'google') {
    const googleUser = {
      id: metadata.id,
      login: metadata.login,
      name: metadata.name,
      avatar: user.image,
    };

    user.accessToken = await getTokenFromAPI('google', googleUser);
    return true;
  }

  return false;
};

callbacks.jwt = async function jwt(token: any, user: any) {
  if (user) {
    token = { accessToken: user.accessToken };
  }

  return token;
};

callbacks.session = async function session(session: any, token: any) {
  session.accessToken = token.accessToken;
  return session;
};

const options = {
  providers,
  callbacks,
};

export default NextAuth(options);
