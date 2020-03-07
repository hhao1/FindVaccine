import React, { Component } from "react";
import { Card, Button, CardTitle, CardText, Row, Col } from "reactstrap";

import {connect} from 'react-redux'

class CardContainer extends Component {


    render(){
        
        const {
            isImportant
        } = this.props

        return(
             <Card body className="pb-0 mb-2" style={{border: isImportant? '2px solid orange' : 'none'}}>
                <CardTitle className="mb-1"><strong className="mr-auto text-primary">{this.props.name}</strong></CardTitle>
                <CardText className="mb-0"><h6><small className="text-muted">{this.props.description}</small></h6></CardText>
                <Row>
                    <Col xs="4"><Button color="link" size="sm">Learn more</Button></Col>
                    <Col xs="2"><Button color="link" size="sm">Locate</Button></Col>
                </Row>
            </Card>
        )
    }

}

export default CardContainer;