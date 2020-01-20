import React, { Fragment } from 'react';

// react-bootstrap component import statements
import { MDBBtn, MDBNavItem} from "mdbreact";

const LoggedInLinks = () => {
    return (
        <MDBNavItem right>
            <Fragment>
            <img src="https://mdbootstrap.com/img/Others/documentation/img(119)-mini.jpg" className="img-circle z-depth-1 rounded-circle" alt="" height="42" width="42"/>
                Ryan Hall
                <MDBBtn color="primary">
                    Logout
                </MDBBtn>
            </Fragment>
        </MDBNavItem>
    )
}

export default LoggedInLinks;