import React, { Component } from "react";
import { Navbar } from "react-bootstrap";
export class Header extends Component {
  render() {
    return (
      <Navbar bg="dark" variant="dark">
        <Navbar.Brand href="#home">Vaccine Finder</Navbar.Brand>
        <Navbar.Toggle />
        <Navbar.Collapse className="justify-content-end"></Navbar.Collapse>
        <Navbar.Collapse className="justify-content-end"></Navbar.Collapse>
        <Navbar.Collapse className="justify-content-end"></Navbar.Collapse>
      </Navbar>
    );
  }
}

export default Header;
