import React, { Component } from "react";
import { Container, Row, Col, Jumbotron, Badge} from "reactstrap";
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

        const {
            vaccines
        } = this.props

        return(

            <Jumbotron className="container mt-4" style={{height: '40em'}}>
                <Container >
                    <Row>

                        <Col xs="6">
                            <Col ref={this.vacinesContainer} className="overflow-auto" style={{'height': '35em'}}>
                                
                                {/* present yellow fever on top of the list */}
                                {vaccines.filter( vaccine => (vaccine.id === 7)).map( vaccine => <CardContainer name={vaccine.name} description={vaccine.detail} key={vaccine.id} isImportant={true}/>)}
                                {vaccines.filter( vaccine => (vaccine.id !== 7)).map( vaccine => <CardContainer name={vaccine.name} description={vaccine.detail} key={vaccine.id}/>)}
                            </Col>
                            
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