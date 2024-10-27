const Razorpay = require("razorpay");
const instance = new Razorpay({
  key_id: "rzp_test_sg_87Tmkobfn79N6M",
  key_secret: "MJHbg7qttUrcwPDF8W37OSZf",
});

const checkout = async (req, res) => {
  const { amount } = req.body;
  const option = {
    amount: amount * 100,
    currency: "AUD",
  };
  const order = await instance.orders.create(option);
  res.json({
    success: true,
    order,
  });
};

const paymentVerification = async (req, res) => {
  const { razorpayOrderId, razorpayPaymentId } = req.body;
  res.json({
    razorpayOrderId,
    razorpayPaymentId,
  });
};

module.exports = {
  checkout,
  paymentVerification,
};
