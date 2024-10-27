import React from 'react';
import { Swiper, SwiperSlide } from 'swiper/react';
import 'swiper/css';
import 'swiper/css/navigation';
import 'swiper/css/pagination';
import { Navigation, Pagination, Autoplay } from 'swiper/modules';

import './HomeSlider.css';

const HomeSlider = () => {
    
  return (
    <div className="home-slider reduced-height">
      <Swiper
        modules={[Navigation, Pagination, Autoplay]}
        navigation
        pagination={{ clickable: true }}
        autoplay={{ delay: 3000, disableOnInteraction: false }}
        loop={true}
        spaceBetween={20}
        slidesPerView={1}
      >
        {/* Main Banner Slide */}
        <SwiperSlide>
          <div className="main-banner position-relative">
            <img
              src="http://127.0.0.1:5000/pythonscripts/projectexports/main-banner-2.jpg"
              className="img-fluid rounded-3 w-100 h-100"
              alt="main banner"
            />
            <a href="/product" className="button-centered">Shop Now</a>
          </div>
        </SwiperSlide>

        {/* Small Banners as Slides */}
        <SwiperSlide>
          <div className="small-banner position-relative">
            <img
              src="http://127.0.0.1:5000/pythonscripts/projectexports/main-banner-2.jpg"
              className="img-fluid rounded-3 w-100 h-100"
              alt="small banner"
            />
            <a href="/product" className="button-centered">Shop Now</a>
          </div>
        </SwiperSlide>

        <SwiperSlide>
          <div className="small-banner position-relative">
            <img
              src="http://127.0.0.1:5000/pythonscripts/projectexports/main-banner-2.jpg"
              className="img-fluid rounded-3 w-100 h-100"
              alt="small banner"
            />
            <a href="/product" className="button-centered">Shop Now</a>
          </div>
        </SwiperSlide>

        <SwiperSlide>
          <div className="small-banner position-relative">
            <img
              src="http://127.0.0.1:5000/pythonscripts/projectexports/main-banner-2.jpg"
              className="img-fluid rounded-3 w-100 h-100"
              alt="small banner"
            />
            <a href="/product" className="button-centered">Shop Now</a>
          </div>
        </SwiperSlide>
      </Swiper>
    </div>
  );
};

export default HomeSlider;
