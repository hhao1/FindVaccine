import React, { Component } from "react";
import { Navbar } from "react-bootstrap";

import { Link, withRouter } from 'react-router-dom'
import {connect} from 'react-redux'

class VirusDetail extends Component {

    render(){

        return(

            <div>
                VirusDetail Page
            </div>
        )
    }
}

export default withRouter(connect(null, null)(VirusDetail));