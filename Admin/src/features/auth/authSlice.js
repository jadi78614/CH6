import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import authService from "./authServices";
import { toast } from "react-toastify";

// Retrieve user from local storage
const getUserfromLocalStorage = localStorage.getItem("user")
  ? JSON.parse(localStorage.getItem("user"))
  : null;

// Initial state
const initialState = {
  user: getUserfromLocalStorage,
  orders: [],
  isError: false,
  isLoading: false,
  isSuccess: false,
  message: "",
};

// Async thunk for login
export const login = createAsyncThunk(
  "auth/login",
  async (userData, thunkAPI) => {
    try {
      console.log("Values in authSlice.js", userData);
      return await authService.login(userData);
    } catch (error) {
      console.log('Login error:', error.response);
      return thunkAPI.rejectWithValue(error.response?.data?.message || error.message);
    }
  }
);

// Async thunk for getting orders
export const getOrders = createAsyncThunk(
  "order/get-orders",
  async (data, thunkAPI) => {
    try {
      return await authService.getOrders(data);
    } catch (error) {
      return thunkAPI.rejectWithValue(error.response?.data?.message || error.message);
    }
  }
);

// Async thunk for getting a single order
export const getaOrder = createAsyncThunk(
  "order/get-order",
  async (id, thunkAPI) => {
    try {
      return await authService.getOrder(id);
    } catch (error) {
      return thunkAPI.rejectWithValue(error.response?.data?.message || error.message);
    }
  }
);

// Async thunk for updating an order
export const updateAOrder = createAsyncThunk(
  "order/update-order",
  async (data, thunkAPI) => {
    try {
      return await authService.updateOrder(data);
    } catch (error) {
      return thunkAPI.rejectWithValue(error.response?.data?.message || error.message);
    }
  }
);

// Async thunk for getting monthly data
export const getMonthlyData = createAsyncThunk(
  "orders/monthlydata",
  async (data, thunkAPI) => {
    try {
      return await authService.getMonthlyOrders(data);
    } catch (error) {
      return thunkAPI.rejectWithValue(error.response?.data?.message || error.message);
    }
  }
);

// Async thunk for getting yearly data
export const getYearlyData = createAsyncThunk(
  "orders/yearlydata",
  async (data, thunkAPI) => {
    try {
      return await authService.getYearlyStats(data);
    } catch (error) {
      return thunkAPI.rejectWithValue(error.response?.data?.message || error.message);
    }
  }
);

// Auth slice
export const authSlice = createSlice({
  name: "auth",
  initialState: initialState,
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(login.pending, (state) => {
        state.isLoading = true;
        state.isSuccess = false; // Reset success state
        state.isError = false;   // Reset error state
      })
      .addCase(login.fulfilled, (state, action) => {
        state.isError = false;
        state.isLoading = false;
        state.isSuccess = true;
        state.user = action.payload;
        state.message = "success";
        state.orders = []; // Clear orders on successful login
      })
      .addCase(login.rejected, (state, action) => {
        state.isError = true;
        state.isSuccess = false;
        state.message = action.error.message || "Login failed"; // Use a meaningful error message
        state.isLoading = false;
        toast.error("Login failed: " + action.error.message); // Notify the user
      })
      .addCase(getOrders.pending, (state) => {
        state.isLoading = true;
        state.isSuccess = false; // Reset success state
        state.isError = false;   // Reset error state
      })
      .addCase(getOrders.fulfilled, (state, action) => {
        state.isError = false;
        state.isLoading = false;
        state.isSuccess = true;
        state.orders = action.payload;
        state.message = "success";
      })
      .addCase(getOrders.rejected, (state, action) => {
        state.isError = true;
        state.isSuccess = false;
        state.message = action.error.message; // Use a meaningful error message
        state.isLoading = false;
        toast.error("Failed to fetch orders: " + action.error.message); // Notify the user
      })
      .addCase(updateAOrder.pending, (state) => {
        state.isLoading = true;
        state.isSuccess = false; // Reset success state
        state.isError = false;   // Reset error state
      })
      .addCase(updateAOrder.fulfilled, (state, action) => {
        state.isError = false;
        state.isLoading = false;
        state.isSuccess = true;
        state.updateorder = action.payload;
        toast.success("Order Status Changed");
      })
      .addCase(updateAOrder.rejected, (state, action) => {
        state.isError = true;
        state.isSuccess = false;
        state.message = action.error.message; // Use a meaningful error message
        state.isLoading = false;
        toast.error("Failed to update order: " + action.error.message); // Notify the user
      })
      .addCase(getaOrder.pending, (state) => {
        state.isLoading = true;
        state.isSuccess = false; // Reset success state
        state.isError = false;   // Reset error state
      })
      .addCase(getaOrder.fulfilled, (state, action) => {
        state.isError = false;
        state.isLoading = false;
        state.isSuccess = true;
        state.singleorder = action.payload;
        state.message = "success";
      })
      .addCase(getaOrder.rejected, (state, action) => {
        state.isError = true;
        state.isSuccess = false;
        state.message = action.error.message; // Use a meaningful error message
        state.isLoading = false;
        toast.error("Failed to fetch order: " + action.error.message); // Notify the user
      })
      .addCase(getMonthlyData.pending, (state) => {
        state.isLoading = true;
        state.isSuccess = false; // Reset success state
        state.isError = false;   // Reset error state
      })
      .addCase(getMonthlyData.fulfilled, (state, action) => {
        state.isError = false;
        state.isLoading = false;
        state.isSuccess = true;
        state.monthlyData = action.payload;
        state.message = "success";
      })
      .addCase(getMonthlyData.rejected, (state, action) => {
        state.isError = true;
        state.isSuccess = false;
        state.message = action.error.message; // Use a meaningful error message
        state.isLoading = false;
        toast.error("Failed to fetch monthly data: " + action.error.message); // Notify the user
      })
      .addCase(getYearlyData.pending, (state) => {
        state.isLoading = true;
        state.isSuccess = false; // Reset success state
        state.isError = false;   // Reset error state
      })
      .addCase(getYearlyData.fulfilled, (state, action) => {
        state.isError = false;
        state.isLoading = false;
        state.isSuccess = true;
        state.yearlyData = action.payload;
        state.message = "success";
      })
      .addCase(getYearlyData.rejected, (state, action) => {
        state.isError = true;
        state.isSuccess = false;
        state.message = action.error.message; // Use a meaningful error message
        state.isLoading = false;
        toast.error("Failed to fetch yearly data: " + action.error.message); // Notify the user
      });
  },
});

export default authSlice.reducer;
