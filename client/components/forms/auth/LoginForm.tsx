import { useState } from 'react';
import { useRouter } from 'next/router';
import { SubmitHandler, useForm } from 'react-hook-form';
import Alert from 'react-bootstrap/Alert';
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
import useAxios from '@/lib/utils/axios';
import { useAppDispatch } from '@/lib/store/redux';
import { userLogin } from '@/lib/store/authSlice';
import { useLogin } from '@/lib/auth';

// wip
interface LoginFormInputs {
  email: string;
  password: string;
}

const LoginForm = () => {
  const dispatch = useAppDispatch();
  const api = useAxios();
  const router = useRouter();
  const [error, setError] = useState('');
  const USER_LOCAL_STORAGE_KEY = 'USER_KEY';
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<LoginFormInputs>();

  const onSubmit: SubmitHandler<LoginFormInputs> = async (data) => {
    setError('');
    try {
      console.log(data);
      // eslint-disable-next-line react-hooks/rules-of-hooks
      const response = await useLogin(data);
      console.log('response', response);
      console.log('response.status ', response.status);
      const user = response.data;
      dispatch(userLogin(user));

      if (response.status === 403) {
        setError(response.data.errors.detail);
      }
      if (response.status === 400) {
        setError(response.data.message);
      }
      if (response.status === 200) {
        localStorage.setItem(USER_LOCAL_STORAGE_KEY, JSON.stringify(user));
        localStorage.setItem('AUTHTOKEN', JSON.stringify(await user.token));
        router.push('/profile');
      }
    } catch (error: any) {
      console.error('error', error);
      console.log('error.response.data.message', error.response.data.message);
      setError(error.response.data.message);
    }
  };
  return (
    <>
      {error ? <Alert variant="danger">{error}</Alert> : null}
      <Form onSubmit={handleSubmit(onSubmit)}>
        <Form.Group className="mb-3" controlId="loginFormEmail">
          <Form.Label>Email address</Form.Label>
          <Form.Control
            type="email"
            placeholder="Enter email"
            defaultValue={router.query.email ? router.query.email : ''}
            {...register('email')}
          />
        </Form.Group>

        <Form.Group className="mb-3" controlId="loginFormPassword">
          <Form.Label>Password</Form.Label>
          <Form.Control
            type="password"
            placeholder="Password"
            {...register('password')}
          />
        </Form.Group>
        <Button variant="primary" type="submit">
          Submit
        </Button>
      </Form>
    </>
  );
};

export default LoginForm;
