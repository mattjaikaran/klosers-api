import { useEffect, useState } from 'react';
import Head from 'next/head';
import MainLayout from '@/layouts/MainLayout';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Button from 'react-bootstrap/Button';
import YTDStatsTable from '@/components/tables/YTDStatsTable';
import CareerStatsTable from '@/components/tables/CareerStatsTable';
import careerStats from '@/data/career-stats.json';
import ytdStats from '@/data/ytd-stats.json';
import AwardsRecognition from '@/components/AwardsRecognition';
import useAxios from '@/lib/utils/axios';
import { useRouter } from 'next/router';

const sampleUserDetails = {
  id: 1,
  first_name: 'JD',
  last_name: 'Reichenbach',
  full_name: 'JD Reichenbach',
  title: 'Strategic Account Executive',
  company: 'NerdWallet',
  market: 'SMB',
  all_time_revenue: '4.5m',
  linkedin_profile: 'https://linkedin.com/in/mattjaikaran',
  fit_score: 90,
};

export default function Profile() {
  const api = useAxios();
  const router = useRouter();
  const [userDetails, setUserDetails] = useState<any>(sampleUserDetails);
  // useEffect(() => {
  //   const renderUserData = async () => {
  //     try {
  //       const response = await api.get('/user');
  //       console.log('response', response);
  //       console.log('response.data', response.data);
  //       setUserDetails(response.data.details)
  //       return response;
  //     } catch (error) {
  //       console.error('error', error);
  //     }
  //   };
  //   renderUserData();
  // }, []);
  return (
    <>
      <Head>
        <title>Profile | Kloser Sales Platform</title>
        <meta name="description" content="Kloser sales platform" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <MainLayout>
        <Container>
          <h1>Profile</h1>
          <Row>
            <Col>
              <p>
                <strong>User: </strong>
                <span>{userDetails.full_name}</span>
              </p>
              <p>
                <strong>Title: </strong>
                <span>{userDetails.title}</span>
              </p>
              <p>
                <strong>Company: </strong>
                <span>{userDetails.company}</span>
              </p>
              <p>
                <strong>Market: </strong>
                <span>{userDetails.market}</span>
              </p>
              <p>
                <strong>All Time Revenue: </strong>
                <span>{userDetails.all_time_revenue}</span>
              </p>
              <p>
                <a href={userDetails.linkedin_profile} target="_blank">
                  LinkedIn
                </a>
              </p>
            </Col>
            <Col>
              <h4>Klosers fit score.</h4>
              <h2>{userDetails.fit_score}%</h2>
              <p>
                Weighted score based on high value categories to fit your
                company profile and parameters.
              </p>
              <Button onClick={() => router.push('/leaderboard')}>
                Kloser Leaderboard
              </Button>
            </Col>
          </Row>
          <h5>YTD Stats</h5>
          <YTDStatsTable data={ytdStats} />
          <h5>Career Stats</h5>
          <CareerStatsTable data={careerStats} />

          <AwardsRecognition />
        </Container>
      </MainLayout>
    </>
  );
}
