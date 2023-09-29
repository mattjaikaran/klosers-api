import { useEffect, useState } from 'react';
import Head from 'next/head';
import AuthLayout from '@/layouts/AuthLayout';
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
import { useAppSelector } from '@/lib/store/redux';

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
  const { user }: any = useAppSelector((state) => state.auth);
  const [userDetails, setUserDetails] = useState<any>(user.data);
  const [userYtdStats, setUserYtdStats] = useState<any>([]);
  const [userCareerStats, setUserCareerStats] = useState<any>([]);
  const [userAwards, setUserAwards] = useState<any>([]);
  useEffect(() => {
    const renderUserData = async () => {
      try {
        const ytdResponse = await api.get('/ytd-stats/');
        const careerResponse = await api.get('/career-stats/');
        // const awardResponse = await api.get('/awards-recognition-stats/');
        setUserYtdStats(ytdResponse.data);
        setUserCareerStats(careerResponse.data);
        // setUserAwards(awardResponse.data);
      } catch (error) {
        console.error('error', error);
      }
    };
    renderUserData();
  }, []);
  return (
    <>
      <Head>
        <title>Profile | Kloser Sales Platform</title>
        <meta name="description" content="Kloser sales platform" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <AuthLayout>
        <Container>
          <h2>Profile</h2>
          <Row className="mt-3">
            <Col md={6}>
              <Row>
                <Col>
                  {/* eslint-disable-next-line @next/next/no-img-element */}
                  <img
                    className="img-fluid"
                    src="https://dummyimage.com/500x400/000/fff"
                    alt=""
                  />
                </Col>
                <Col>
                  <p>
                    <strong>Name: </strong>
                    <span>
                      {userDetails.first_name} {userDetails.last_name}
                    </span>
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
                    <span>{userDetails.market_type}</span>
                  </p>
                  <p>
                    <strong>All Time Revenue: </strong>
                    <span>
                      $
                      {parseInt(userDetails.all_time_revenue).toLocaleString(
                        'en-US'
                      )}
                    </span>
                  </p>
                  <p>
                    <a href={userDetails.linkedin_profile} target="_blank">
                      LinkedIn
                    </a>
                  </p>
                </Col>
              </Row>
            </Col>
            <Col md={6} className="text-center">
              <h1 className="d-inline">
                <span className="with-marker">Klosers</span>{' '}
              </h1>
              <h2 className="d-inline">
                <span>fit score.</span>
              </h2>
              <h2 className="text-primary">{userDetails.user_fit_score}%</h2>
              <p className="px-md-5">
                Weighted score based on high value categories to fit your
                company profile and parameters.
              </p>
              <Button
                className="pill-btn"
                onClick={() => router.push('/leaderboard')}
              >
                Kloser Leaderboard {'>'}
              </Button>
            </Col>
          </Row>
          <h5>YTD Stats</h5>
          <YTDStatsTable data={userYtdStats} />
          <h5>Career Stats</h5>
          <CareerStatsTable data={userCareerStats} />

          <AwardsRecognition />
        </Container>
      </AuthLayout>
    </>
  );
}
