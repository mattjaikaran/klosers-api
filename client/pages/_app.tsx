import '@/styles/globals.scss';
import type { AppProps } from 'next/app';
import { Provider } from 'react-redux';
import { store, persistor } from '@/lib/store';
import { PersistGate } from 'redux-persist/integration/react';
import { SessionProvider } from 'next-auth/react';

// const clientId = process.env.NEXT_PUBLIC_GOOGLE_CLIENT_ID;

// {
//   session ? (
//     <>
//       <p>signed in as {session?.user?.email}</p>
//       <Button onClick={() => signOut()}>Sign out</Button>
//       {/* {session.accessToken && <p>User has access token</p>} */}
//     </>
//   ) : (
//     <>
//       <p>not signed in</p>
//       <Button onClick={() => signIn()}>Sign In via Google </Button>
//       <p>{!session && 'User is not logged in'}</p>
//     </>
//   );
// }

export default function App({
  Component,
  pageProps: { session, ...pageProps },
}: AppProps) {
  return (
    <Provider store={store}>
      <SessionProvider session={session}>
        <PersistGate loading={null} persistor={persistor}>
          <Component {...pageProps} />
        </PersistGate>
      </SessionProvider>
    </Provider>
  );
}
