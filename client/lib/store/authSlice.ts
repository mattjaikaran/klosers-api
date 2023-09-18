import { createSlice } from '@reduxjs/toolkit';

const AUTH = 'auth';
const initialState = {
  user: {},
  isLoggedIn: false,
};

export const authSlice = createSlice({
  name: AUTH,
  initialState,
  reducers: {
    //Actions
    userLogin: (state, action) => {
      state.user = {
        ...state.user,
        data: action.payload,
      };
      state.isLoggedIn = true;
    },
    userLogout: (state, action) => {
      state.user = {
        ...state.user,
        data: action.payload,
      };
      state.isLoggedIn = false;
    },
  },
});

export const { userLogin, userLogout } = authSlice.actions;

// //Selectors - this is how we pull information from the global store slice
export const getUser = (state: typeof initialState) => state.user;
export default authSlice.reducer;