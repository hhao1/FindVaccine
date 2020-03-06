import React, { Component } from "react";
import { Navbar } from "react-bootstrap";

import { Link, withRouter } from 'react-router-dom'
import {connect} from 'react-redux'

class Home extends Component {

    render(){

        return(

            <div>
                Home
            </div>
        )
    }
}

export default withRouter(connect(null, null)(Home));