import Head from 'next/head';
import AuthLayout from '@/layouts/AuthLayout';
import Container from 'react-bootstrap/Container';
import Button from 'react-bootstrap/Button';
import { signIn, signOut, useSession, getServerSession } from 'next-auth/react';

export default function Dashboard() {
  const { data: session } = useSession();
  return (
    <div>
      <Head>
        <title>Dashboard | Kloser Sales Platform</title>
        <meta name="description" content="Kloser sales platform" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <AuthLayout>
        <Container>
          <h2>Dashboard</h2>
          {/* <p>signed in as {session?.user?.email}</p>
          <Button onClick={() => signOut()}>Sign out</Button>
          {session?.accessToken && <p>User has access token</p>} */}
        </Container>
      </AuthLayout>
    </div>
  );
}
