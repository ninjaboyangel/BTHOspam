import React, { Component } from 'react';
import { BrowserRouter } from 'react-router-dom';
import LoggedInLinks from './LoggedInLinks'
import LoggedOutLinks from './LoggedOutLinks'

// react-bootstrap component import statements
import { MDBNavbar, MDBNavbarBrand, MDBNavbarNav, MDBNavbarToggler, MDBCollapse, } from "mdbreact";


// asset imports
import brandlogo from '../../assets/image/bthospam_brand_white.png'

class Header extends Component {
  state = {
    collapseID: ""
  };

  toggleCollapse = collapseID => () => {
    this.setState(prevState => ({
      collapseID: prevState.collapseID !== collapseID ? collapseID : ""
    }))
  }
  
  render() {
    const overlay = (
      <div id="sidenav-overlay" style={{ backgroundColor: 'transparent' }} onClick={this.toggleCollapse("navbarCollapse")} />
      );
    return (
      <div>
        <MDBNavbar style={{boxShadow: "none"}} expand="md" fixed="top" color="" dark>
          <MDBNavbarBrand>
              <img style={{height: "60px"}}src={brandlogo} alt="BTHOspam Brand Logo"/>
          </MDBNavbarBrand>
          <MDBNavbarToggler onClick={this.toggleCollapse("navbarCollapse")} />
          <MDBCollapse id="navbarCollapse" isOpen={this.state.collapseID} navbar>
            <MDBNavbarNav right>
              <LoggedOutLinks/>
            </MDBNavbarNav>
          </MDBCollapse>
        </MDBNavbar>
        {this.state.collapseID && overlay}
      </div>
    )
  }
}

export default Header;
