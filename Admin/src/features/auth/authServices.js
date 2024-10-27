import axios from "axios";
import { config } from "../../utils/axiosconfig";
import { base_url } from "../../utils/baseUrl";

// const getTokenFromLocalStorage = localStorage.get("user")
//   ? JSON.parse(localStorage.getItem("user"))
//   : null;



// Login service
const login = async (user) => {
  console.log("Values in authServices.js:", user);
  
  try {
    const response = await axios.post(`${base_url}user/admin-login`, user,{
      headers: {
        'Content-Type': 'application/json', // Set content type
      },
    });
    if (response.data) {
      localStorage.setItem("user", JSON.stringify(response.data));
      console.log("Login successful, user data stored in localStorage");
    }
    console.log("Response from login API:", response.data);
    return response.data;
  } catch (error) {
    console.error("Login error:", error.response ? error.response.data : error.message);
    throw error; // Re-throw the error to be handled in the slice
  }
};

const getOrders = async (data) => {
  const response = await axios.get(`${base_url}user/getallorders`, data);

  return response.data;
};
const getOrder = async (id) => {
  const response = await axios.get(
    `${base_url}user/getaOrder/${id}`,

    config
  );

  return response.data;
};

const updateOrder = async (data) => {
  const response = await axios.put(
    `${base_url}user/updateOrder/${data.id}`,
    { status: data.status },
    config
  );

  return response.data;
};

const getMonthlyOrders = async (data) => {
  const response = await axios.get(
    `${base_url}user/getMonthWiseOrderIncome`,

    data
  );

  return response.data;
};

const getYearlyStats = async (data) => {
  const response = await axios.get(
    `${base_url}user/getyearlyorders`,

    data
  );

  return response.data;
};

const authService = {
  login,
  getOrders,
  getOrder,
  getMonthlyOrders,
  getYearlyStats,
  updateOrder,
};

export default authService;
