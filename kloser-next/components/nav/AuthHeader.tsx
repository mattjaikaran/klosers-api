import { useLogin, useLogout } from '@/lib/auth';
import Link from 'next/link';
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';

const AuthHeader = ({
  user,
  isLoggedIn,
}: {
  user: any;
  isLoggedIn: boolean;
}) => {
  console.log('user', user);
  return (
    <Navbar collapseOnSelect expand="lg" className="bg-body-tertiary">
      <Container>
        <Navbar.Brand as={Link} href="/">
          Klosers
        </Navbar.Brand>
        <Navbar.Toggle aria-controls="responsive-navbar-nav" />
        <Navbar.Collapse id="responsive-navbar-nav">
          <Nav className="me-auto">
            <Nav.Link as={Link} href="/">
              Dashboard
            </Nav.Link>
            <Nav.Link as={Link} href="/profile">
              Profile
            </Nav.Link>
            {/* eslint-disable-next-line react-hooks/rules-of-hooks */}
            <Nav.Link onClick={() => useLogout(user)}>Logout</Nav.Link>
          </Nav>
          <Nav>
            <Nav.Link as={Link} href="/">
              Kloser Network
            </Nav.Link>
            <Nav.Link eventKey={2} as={Link} href="/leaderboard">
              Kloser Leaderboard
            </Nav.Link>
            {/* <Nav.Link as={Link} href="/">
              Twitter
            </Nav.Link>
            <Nav.Link as={Link} href="/">
              LinkedIn
            </Nav.Link> */}
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
};

export default AuthHeader;
