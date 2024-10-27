



//------------------------------------------------------------------------------------------------------------------------




import React, { useEffect, useState } from "react";
import ReactStars from "react-rating-stars-component";
import BreadCrumb from "../components/BreadCrumb";
import Meta from "../components/Meta";
import ProductCard from "../components/ProductCard";
import ReactImageZoom from "react-image-zoom";
import Color from "../components/Color";
import { AiOutlineHeart, AiFillHeart } from "react-icons/ai";
import { useLocation, useNavigate } from "react-router-dom";
import Container from "../components/Container";
import { useDispatch, useSelector } from "react-redux";
import { addRating, getAProduct, getAllProducts } from "../features/products/productSlilce";
import { toast } from "react-toastify";
import { addProdToCart, getUserCart } from "../features/user/userSlice";
import { Modal, Button } from 'react-bootstrap';
import axios from 'axios';

const SingleProduct = () => {
  const [color, setColor] = useState(null);
  const [quantity, setQuantity] = useState(1);
  const [alreadyAdded, setAlreadyAdded] = useState(false);
  const [show, setShow] = useState(false);
  const [popularProduct, setPopularProduct] = useState([]);
  const [star, setStar] = useState(null);
  const [comment, setComment] = useState(null);
  const [isFilled, setIsFilled] = useState(false);
  const [waist, setWaist] = useState(""); 
  const [height, setHeight] = useState(""); 
  const [modelSrc, setModelSrc] = useState(""); 
  const [previewImage, setPreviewImage] = useState(""); 

  const location = useLocation();
  const navigate = useNavigate();
  const getProductId = location.pathname.split("/")[2];
  const dispatch = useDispatch();

  const productState = useSelector((state) => state?.product?.singleproduct);
  const productsState = useSelector((state) => state?.product?.product);
  const cartState = useSelector((state) => state?.auth?.cartProducts);
  const productsLoading = useSelector((state) => state?.product?.loading);


  useEffect(() => {
    // Check if productState and productState._id exist
    if (productState && productState._id) {
      const productId = productState._id;
      console.log('Product ID:', productId);

      // Perform any action that requires productId
      // Example: Making a request to download images based on productId
      fetch(`http://localhost:4002/api/product/saveimages/${productId}`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
        },
      })
        .then((response) => response.json())
        .then((data) => {
          console.log('Response:', data);
        })
        .catch((error) => {
          console.error('Error:', error);
        });
    }
  }, [productState]); // Re-run the effect when productState changes




  useEffect(() => {
    dispatch(getAProduct(getProductId));
    dispatch(getUserCart());
    dispatch(getAllProducts());
  }, [dispatch, getProductId]);

  useEffect(() => {
    if (productState?.images?.length > 0) {
      setPreviewImage(productState.images[0].url);
    }
  }, [productState]);

  useEffect(() => {
    if (Array.isArray(cartState)) {
      cartState.forEach((item) => {
        if (getProductId === item?.productId?._id) {
          setAlreadyAdded(true);
        }
      });
    }
  }, [cartState, getProductId]);

  useEffect(() => {
    if (!productsLoading && Array.isArray(productsState)) {
      const data = productsState.filter((item) => item.tags === "popular");
      setPopularProduct(data);
    }
  }, [productsState, productsLoading]);

  useEffect(() => {
    // Load the <model-viewer> script
    const script = document.createElement('script');
    script.type = 'module';
    script.src = 'https://ajax.googleapis.com/ajax/libs/model-viewer/3.5.0/model-viewer.min.js';
    document.body.appendChild(script);
  }, []);

  const uploadCart = () => {
    if (color === null) {
      toast.error("Please choose a color");
    } else {
      dispatch(
        addProdToCart({
          productId: productState?._id,
          quantity,
          color,
          price: productState?.price,
        })
      );
      navigate("/cart");
    }
  };

  // const handleModelRender = async (e) => {
  //   e.preventDefault(); 
  //   // Validate waist and height inputs
  //   if (!waist || !height) {
  //     toast.error("Please enter both waist and height");
  //     return;
  //   }

  //   try {
  //     // Step 1: Request model generation from backend
  //     const response = await axios.post("http://127.0.0.1:5000/", {
  //       "head": "0.95",
  //       "torso": "0.89",
  //       "legs": "1.10",
  //       "calves": "0.90",
  //       "shoulders": "0.80",
  //       "arms": "0.85",
  //       "forearms": "0.85",
  //       "hips": waist.toString(),
  //       "height": height.toString(),
  //     });
      

  //     if (response.status==202) {
  //       // Step 2: Set the generated model's path
  //       setModelSrc("/images/model.glb");

  //       toast.success("Model generated successfully!");
  //     } else {
  //       toast.error("Model generation failed.");
  //     }
  //   } catch (error) {
  //     toast.error(`Failed to generate the model. Status: `);
  //     console.error("Error:", error);
  //   }
  // };



  const handleModelRender = (e,productState) => {

    
    productState.map((item, index) => {
      console.log("Urlssss are ",item.url,index)
    })

    // e.preventDefault();
  
    // Validate waist and height inputs
    if (!waist || !height) {
      toast.error("Please enter both waist and height");
      return;
    }
  
    // Create a new XMLHttpRequest object
    const xhr = new XMLHttpRequest();
    xhr.open("POST", "http://127.0.0.1:5000/", true);
    xhr.setRequestHeader("Content-Type", "application/json");
  
    // Handle the response
    xhr.onreadystatechange = function () {
      if (xhr.readyState === 4) {
        if (xhr.status === 202) {
          // Success: Set the generated model's path
          setModelSrc("http://127.0.0.1:5000/pythonscripts/projectexports/model.glb");
          
          toast.success("Model generated successfully!");
          
        } else {
          // Error handling
          toast.error(`Model generation failed. Status: ${xhr.status}`);
        }
      }
    };
    //  const waist2 = waist === 1.10 ? 1 : (waist / 30) - 0.12;
    //  const height2 = height === 1.10 ? 1 : (height / 65) - 0.09;
     const width_scale = waist / 35;  // Use 35 as a more realistic average waist
     const height_scale = height / 70; 
    // Prepare the request payload
    const payload = JSON.stringify({
      head: "0.95",
      torso: "0.89",
      legs: "1.10",
      calves: "0.90",
      shoulders: "0.80",
      arms: "0.85",
      forearms: "0.85",
      hips: width_scale.toString(),
      height: height_scale.toString(),
    });
  
    // Send the request
    xhr.send(payload);
  };
  

  





  return (
    <>
      <Meta title={"Product Name"} />
      <BreadCrumb title={productState?.title} />
      <Container class1="main-product-wrapper py-5 home-wrapper-2">
        <div className="row">
          <div className="col-6">
            <div className="main-product-image">
              <ReactImageZoom
                width={594}
                height={600}
                zoomWidth={600}
                img={previewImage || "https://images.pexels.com/photos/190819/pexels-photo-190819.jpeg?cs=srgb&dl=pexels-fernando-arcos-190819.jpg&fm=jpg"}
              />
            </div>
            <div className="other-product-images d-flex flex-wrap gap-15">
              {productState?.images.map((item, index) => (

                // console.log(item.url)

                <div key={index} onClick={() => setPreviewImage(item.url)}>
                  <img src={item?.url} className="img-fluid" alt="" />
                </div>
              ))}
            </div>
          </div>
          <div className="col-6">
            <div className="main-product-details">
              <div className="border-bottom">
                <h3 className="title">{productState?.title}</h3>
              </div>
              <div className="border-bottom py-3">
                <p className="price"> $ {productState?.price}/-</p>
                <div className="d-flex align-items-center gap-10">
                  <ReactStars
                    count={5}
                    size={24}
                    value={productState?.totalrating?.toString()}
                    edit={false}
                    activeColor="#ffd700"
                  />
                  <p className="mb-0 t-review">
                    ( {productState?.ratings?.length} Reviews )
                  </p>
                </div>
                <a className="review-btn" href="#review">
                  Write a Review
                </a>
              </div>
              <div className="py-3">
                <div className="d-flex gap-10 align-items-center my-2">
                  <h3 className="product-heading">Type :</h3>
                  <p className="product-data">{productState?.category}</p>
                </div>
                <div className="d-flex gap-10 align-items-center my-2">
                  <h3 className="product-heading">Brand :</h3>
                  <p className="product-data">{productState?.brand}</p>
                </div>
                <div className="d-flex gap-10 align-items-center my-2">
                  <h3 className="product-heading">Tags :</h3>
                  <p className="product-data">{productState?.tags}</p>
                </div>
                <div className="d-flex gap-10 align-items-center my-2">
                  <h3 className="product-heading">Availability :</h3>
                  <p className="product-data">In Stock</p>
                </div>
                {!alreadyAdded && (
                  <div className="d-flex gap-10 flex-column mt-2 mb-3">
                    <h3 className="product-heading">Color :</h3>
                    <Color
                      setColor={setColor}
                      colorData={productState?.color}
                    />
                  </div>
                )}
                <div className="d-flex align-items-center gap-15 flex-row mt-2 mb-3">
                  <h3 className="product-heading">Quantity :</h3>
                  {!alreadyAdded && (
                    <div>
                      <input
                        type="number"
                        min={1}
                        max={10}
                        className="form-control"
                        style={{ width: "70px" }}
                        onChange={(e) => setQuantity(e.target.value)}
                        value={quantity}
                      />
                    </div>
                  )}
                  <button
                    className="button border-0"
                    type="button"
                    onClick={() => (alreadyAdded ? navigate("/cart") : uploadCart())}
                  >
                    {alreadyAdded ? "Go to Cart" : "Add to Cart"}
                  </button>
                  <button
                    className="button border-0 mt-3"
                    type="button"
                    onClick={() => setShow(true)}
                  >
                    Try On
                  </button>
                </div>
                <div className="d-flex align-items-center gap-15">
                  <AiFillHeart
                    className={`fs-5 me-2 ${isFilled ? "filled" : ""}`}
                    onClick={() => setIsFilled(!isFilled)}
                  />
                </div>
              </div>
            </div>
          </div>
        </div>
      </Container>

      {/* Modal with inputs for waist and height */}
      <Modal
        show={show}
        onHide={() => {
          setShow(false);
          setModelSrc("");
          setTimeout(() => {
            setModelSrc(""); // Reset to reload the model
          }, 1); // Reset the model source to trigger reload
        }}
        size="lg"
        centered
        dialogClassName="custom-modal-size"
      >
        <Modal.Header closeButton>
          <Modal.Title>Try On</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          {!modelSrc ? (
            <div>
              <div className="input-group mb-3">
                <input
                  type="text"
                  className="form-control"
                  placeholder="Enter Waist in inches "
                  value={waist}
                  onChange={(e) => setWaist(e.target.value)}
                />
              </div>
              <div className="input-group mb-3">
                <input
                  type="text"
                  className="form-control"
                  placeholder="Enter Height in inches"
                  value={height}
                  onChange={(e) => setHeight(e.target.value)}
                />
              </div>
              <Button  type="button" variant="primary" onClick={(e) => handleModelRender(e,productState?.images)} >
                Generate Model

              </Button>
            </div>
          ) : (
            <div style={{ height: "50vh", width: "100%" }}>
              <model-viewer
                src={modelSrc}
                alt="3D Model"
                ar
                environment-image="neutral"
                shadow-intensity="1"
                camera-controls
                touch-action="pan-y"
                style={{ width: '100%', height: '100%' }}
              />
            </div>
          )}
        </Modal.Body>
      </Modal>

      <Container class1="popular-wrapper py-5 home-wrapper-2">
        <h3 className="section-heading">Our Popular Products</h3>
        <div className="row">
          {popularProduct.map((item, index) => (
            <div className="col-3" key={index}>
              <ProductCard item={item} />
            </div>
          ))}
        </div>
      </Container>
    </>
  );
};

export default SingleProduct;




//------------------------------------------------------------------------------------------------------------------------

