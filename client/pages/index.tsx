import Head from 'next/head';
import { useRouter } from 'next/router';
import MainLayout from '@/layouts/MainLayout';
import Container from 'react-bootstrap/Container';
import Button from 'react-bootstrap/Button';
import { signIn, signOut, useSession } from 'next-auth/react';
import styles from '@/styles/Home.module.css';

export default function Home() {
  const router = useRouter();

  const { data: session } = useSession();
  console.log('session', session);

  return (
    <>
      <Head>
        <title>Kloser Sales Platform</title>
        <meta name="description" content="Kloser sales platform" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <MainLayout>
        <Container>
          <h1 className="mt-5">Klosers</h1>
          <h3 className="mt-5">Sign-up for FREE</h3>
          <p>
            An exclusive network where top sale talent share stats, and leverage
            past performance to match with future job prospects.
          </p>
          <p>Be on Every CEO & VPs 🔥 list.</p>
          <div className="d-grid d-md-inline gap-2">
            <Button
              variant="outline-primary"
              onClick={() => router.push('/signup')}
            >
              Create an Account
            </Button>
            <Button onClick={() => router.push('/signin')}>
              Already have an Account?
            </Button>
          </div>
        </Container>
      </MainLayout>
    </>
  );
}
