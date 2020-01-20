import React, { Fragment } from 'react';

// react-bootstrap component import statements
import { MDBNavItem, MDBBtn, MDBIcon } from 'mdbreact'

const LoggedOutLinks = () => {
    return (
        <MDBNavItem right>
            <Fragment>
                <MDBBtn color="primary">
                    Sign in with <MDBIcon fab icon="google" className="ml-1" />
                </MDBBtn>
            </Fragment>
        </MDBNavItem>
    )
}

export default LoggedOutLinks;