import Header from '@/components/nav/Header';
import { useAppDispatch, useAppSelector } from '@/lib/store/redux';

// @ts-ignore
const MainLayout = ({ children }) => {
  // const dispatch = useAppDispatch();
  // const isLoggedIn = useAppSelector((state) => state.auth?.isLoggedIn);
  // const data: any = useAppSelector((state) => state.auth);
  // const user: any = data.user.data;

  return (
    <div>
      <Header />
      <main className="py-3">{children}</main>
    </div>
  );
};

export default MainLayout;
