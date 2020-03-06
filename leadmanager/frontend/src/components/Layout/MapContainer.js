import React, { Component } from 'react';
import { Map, GoogleApiWrapper } from 'google-maps-react';
import { Card, Button, CardTitle, CardText, Row, Col } from "reactstrap";


import { Key } from '../../config';

const mapStyles = {
    width: '90%',
    height: '15em',
    border: '1px solid gray'
};

class MapContainer extends Component {

    
    render(){

        return(
            <Map
                google={this.props.google}
                zoom={8}
                style={mapStyles}
                initialCenter={{ lat: 47.444, lng: -122.176}}
            />
        )
    }
}

export default GoogleApiWrapper({
    apiKey: Key
  })(MapContainer);