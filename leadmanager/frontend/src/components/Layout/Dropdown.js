import React, { Component } from "react";
import { Form } from "react-bootstrap";

export class Dropdown extends Component {
  render() {
    return (
      <div>
        <Form.Group controlId="exampleForm.ControlSelect1">
          <Form.Label>Select Country</Form.Label>
          <Form.Control as="select">
            <option>1</option>
            <option>2</option>
            <option>3</option>
            <option>4</option>
            <option>5</option>
          </Form.Control>
        </Form.Group>
      </div>
    );
  }
}

export default Dropdown;
