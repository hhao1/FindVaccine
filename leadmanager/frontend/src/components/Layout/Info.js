import React, { Component } from "react";
import { Container, Row, Col, Jumbotron} from "reactstrap";
import PropTypes from "prop-types";
import {connect} from 'react-redux'

import MapContainer from './MapContainer'
import CardContainer from './CardContainer'


import { getVaccines } from "../../actions/vaccines";
import { getMarkers } from "../../actions/markers";

class Info extends Component {

    constructor(props){
        super(props)

        this.vacinesContainer = React.createRef()
    }

    static PropTypes = {
        vaccines: PropTypes.array.isRequired,
        markers: PropTypes.array.isRequired
    };

    handleScroll() {
        
    }
    
    componentDidMount() {
        this.props.getVaccines();
        this.props.getMarkers();
    }

    render(){

        return(

            <Jumbotron className="container mt-4" style={{height: '40em'}}>
                <Container >
                    <Row>
                        <Col ref={this.vacinesContainer} xs="6" className="overflow-auto" style={{'height': '35em'}}>
                            {this.props.vaccines.map(vaccine => <CardContainer name={vaccine.name} description={vaccine.detail} key={vaccine.id}/>)}
                        </Col>

                        <Col xs="6">
                            <MapContainer/>
                        </Col>
                    </Row>
                </Container>

            </Jumbotron>
            
        )
    }
}


const mapStateToProps = state => ({
    vaccines: state.vaccineReducer.vaccines,
    markers: state.markerReducer.markers
  });
  
  export default connect(mapStateToProps, { getVaccines, getMarkers })(Info);