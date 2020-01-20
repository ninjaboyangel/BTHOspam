import React, {Component} from 'react';
import { BrowserRouter } from "react-router-dom";
import ReactRotatingText from 'react-rotating-text'

import styles from './Home.css'
import backgroundVideo from '../../assets/video/bg.mp4'

// react-bootstrap component import statements
import { MDBMask, MDBRow, MDBCol, MDBIcon, MDBBtn, MDBView, MDBContainer } from "mdbreact";

const filter_names = ['athletics', 'UPD crime alert', 'men\'s organization', 'third party', 'international student', 'women\'s organization', 'sorority', 'study abroad', 'paid research opportunity', 'fraternity']
const Home = () => {
    return (
        <div id="videobackground">
            <BrowserRouter>
                <MDBView>
                    <video className="video-intro" playsInline
                    autoPlay muted="false" loop>
                    <source src={backgroundVideo} type="video/mp4" />
                    </video>
                    <MDBMask className="d-flex center align-items-center gradient">
                    <MDBContainer className="px-md-3 px-sm-0">
                        <MDBRow>
                        <MDBCol md="12" className="mb-4 white-text text-center">
                            <h3 className="display-4 font-weight-bold mb-0xz pt-md-1">
                            Let's beat the hell outta </h3>
                            <h3 className="display-4 font-weight-bold mb-0 pt-md-1">
                                <ReactRotatingText items={filter_names}/> emails </h3>
                            <hr className="hr-light my-4 w-75" />
                            <MDBBtn color="primary" outline rounded>
                            Get started <MDBIcon icon="sign-in-alt" /> 
                            </MDBBtn>
                        </MDBCol>
                        </MDBRow>
                    </MDBContainer>
                    </MDBMask>
                </MDBView>
            </BrowserRouter>
        </div>
    )
}

export default Home;