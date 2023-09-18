import axios from 'axios';
import Cookies from 'js-cookie';

export interface UserProps {
  id: string;
  first_name: string;
  last_name: string;
  username: string;
  email: string;
  role?: string;
  token?: string;
}

export interface LoginFormInputs {
  email: string;
  password: string;
}

export interface SignupFormInputs {
  first_name: string;
  last_name: string;
  email: string;
  username: string;
  password: string;
  password_confirmation?: string;
}
export interface PasswordResetInputs {
  newPassword: string;
  newPassword2: string;
  uid: string;
  token: string;
}

export interface SignupResponseData {
  first_name: string;
  last_name: string;
  email: string;
}
import { useAppSelector } from '../store/redux';

export const tokenHeaders = () => {
  // eslint-disable-next-line react-hooks/rules-of-hooks
  const { user }: any = useAppSelector((state) => state.auth);
  const headers = {
    'Content-Type': 'application/json',
    'X-CSRFToken': Cookies.get('csrftoken'),
    sessionid: Cookies.get('sessionid'),
    Authorization: `Bearer ${user?.data?.token}`,
  };
  return headers;
};

const API_URL = process.env.NEXT_PUBLIC_API_URL;

export async function useSignup(data: SignupFormInputs) {
  try {
    const response = await axios.post(`${API_URL}/users/`, data);
    console.log('response', response);
    return response;
  } catch (error: any) {
    console.log('error in useSignup', error);
    return error.response;
  }
}
export async function useLogin(data: LoginFormInputs): Promise<any> {
  try {
    const response = await axios.post(`${API_URL}/login/`, data);
    return response;
  } catch (error: any) {
    console.log('error in useLogin', error);
    return error.response;
  }
}

export async function useLogout(user: UserProps): Promise<any> {
  try {
    const response = await axios.post(`${API_URL}/logout/`, user.email);
    console.log('response', response);
    if (response) {
      localStorage.clear();
      return response;
    }
  } catch (error: any) {
    console.log('error in useLogout', error);
    return error.response;
  }
}

export async function useForgotPassword(email: string) {
  try {
    const data = { email: email.toLowerCase() };
    const response = await axios.post(`${API_URL}/password/reset/`, data);
    console.log('response', response);
    return response.data;
  } catch (error: any) {
    console.log('error in useForgotPassword', error);
    return error.response;
  }
}

export async function usePasswordReset(data: PasswordResetInputs) {
  try {
    const response = await axios.post(
      `${API_URL}/password/reset/confirm/`,
      data
    );
    console.log('response', response);
    return response.data;
  } catch (error: any) {
    console.log('error in useForgotPassword', error);
    return error.response;
  }
}
