import React, { Component } from "react";
import { Toast, ToastBody, ToastHeader } from "reactstrap";

import {connect} from 'react-redux'

class ToastContainer extends Component {

    render(){

        return(

            <div>  
                <Toast>
                    <ToastHeader className="text-right">
                        <strong className="mr-auto text-primary">{this.props.name}</strong>
                    </ToastHeader>
                    
                    <ToastBody>
                        {this.props.description}          
                    </ToastBody>
                </Toast>
            </div>
            
        )
    }

}

export default ToastContainer;