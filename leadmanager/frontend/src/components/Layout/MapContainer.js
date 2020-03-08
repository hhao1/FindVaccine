import React, { Component } from 'react'
import { Map, GoogleApiWrapper, Marker } from 'google-maps-react'
import { Card, Button, CardTitle, CardText, Row, Col } from "reactstrap"


import { Key } from '../../config';
import markers from '../../reducers/markers';

const mapStyles = {
    width: '90%',
    height: '60%',
    border: '1px solid gray'
};

class MapContainer extends Component {

    
    // 
    render(){

        const {
            markers
        } = this.props

        const userLocation = {lat: 49.1755761, lng: -123.14568639999997}

        var bounds = new this.props.google.maps.LatLngBounds()


        return(
            <Map
                google={this.props.google}
                style={mapStyles}
                zoom={10}
                initialCenter={userLocation}
                // bounds={bounds}
                >

                {/* {markers.map( marker => <Marker name={marker.name} position={{lat: marker.lat, lng: marker.lon}} key={marker.id}/>)} */}
            </Map>
                
        )
    }
}

export default GoogleApiWrapper({
    apiKey: Key
  })(MapContainer);