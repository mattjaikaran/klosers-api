import Head from 'next/head';
import Container from 'react-bootstrap/Container';
import Button from 'react-bootstrap/Button';
import LoginForm from '@/components/forms/auth/LoginForm';
import MainLayout from '@/layouts/MainLayout';
import { signIn, signOut, useSession } from 'next-auth/react';
export default function Signin() {
  const { data: session } = useSession();
  console.log('session', session);
  return (
    <>
      <Head>
        <title>Login | Kloser Sales Platform</title>
        <meta name="description" content="Kloser sales platform" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <MainLayout>
        <Container>
          <h1>Sign In</h1>
          <LoginForm />
          {session ? (
            <>
              <p>signed in as {session?.user?.email}</p>
              <Button onClick={() => signOut()}>Sign out</Button>
              {/* {session.accessToken && <p>User has access token</p>} */}
            </>
          ) : (
            <>
              <p>not signed in</p>
              <Button onClick={() => signIn('google').catch()}>
                Sign In via Google{' '}
              </Button>
              <p>{!session && 'User is not logged in'}</p>
            </>
          )}
        </Container>
      </MainLayout>
    </>
  );
}