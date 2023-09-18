import AuthHeader from '@/components/nav/AuthHeader';
import { userLogout } from '@/lib/store/authSlice';
import { useAppDispatch, useAppSelector } from '@/lib/store/redux';
import { useRouter } from 'next/router';
import { useMemo } from 'react';

// @ts-ignore
const AuthLayout = ({ children }) => {
  const dispatch = useAppDispatch();
  const isLoggedIn = useAppSelector((state) => state.auth?.isLoggedIn);
  const router = useRouter();
  const data: any = useAppSelector((state) => state.auth);
  const user: any = data.user.data;

  useMemo(() => {
    if (!user || !isLoggedIn) {
      dispatch(userLogout(user));
      router.push('/');
    }
  }, [user, isLoggedIn, router, dispatch]);

  return (
    <div>
      <AuthHeader user={user} isLoggedIn={isLoggedIn} />
      <main className="py-3">{children}</main>
    </div>
  );
};

export default AuthLayout;
