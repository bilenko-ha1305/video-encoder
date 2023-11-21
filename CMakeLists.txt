cmake_minimum_required(VERSION 3.24)
project(video_encoder)

set(CMAKE_CXX_STANDARD 14)

include_directories(video-encoder/cpp)

add_executable(video_encoder
        video-encoder/cpp/lodepng.cpp
        video-encoder/cpp/lodepng.h
        video-encoder/cpp/main.cpp
        video-encoder/cpp/main.h)
