import React, { Component } from 'react';

import { MDBMask, MDBRow, MDBCol, MDBIcon, MDBBtn, MDBView, MDBContainer } from "mdbreact";
import style from './Dashboard.css'

class Dashboard extends Component {
    state = {
        filters: [
            "Athletic Updates",
            "Barnes and Noble",
            "Blue Baker",
            "Fraternities",
            "International Students",
            "Men's Organizations",
            "Opportunities Abroad",
            "Paid Research Opportunities",
            "Piazza",
            "Research",
            "Sororities",
            "Today Subscribers",
            "UPD Crime Alerts",
            "Women's Organizations"
        ]
    }

    handleChange = (e) => {
        console.log(e)
    }

    handleSubmit = (e) => {
        console.log(e)
    }
    
    renderFilters = () => {
        return this.state.filters.map((e) => {
                return (
                    <div>
                        <input
                        type = 'checkbox'
                        className='custom-control-input'
                        id='customSwitches'
                        />
                        <label className='custom-control-label' htmlFor='customSwitches'>
                            {e}
                        </label>
                    </div>
                )
            })
    }
    render() {
        return (
            <MDBMask className="d-flex justify-content-center align-items-center gradient">
                    <MDBContainer className="px-md-3 px-sm-0">
                        <MDBRow>
                        <MDBCol md="12" className="mb-4 black-text centered">
                            <p>Select what you would like to filter out of your inbox.</p>
                            <div className='custom-control custom-switch'>
                                {this.renderFilters()}
                            </div>

                        </MDBCol>
                        </MDBRow>
                    </MDBContainer>
                    </MDBMask>
        )
    }
}

export default Dashboard;