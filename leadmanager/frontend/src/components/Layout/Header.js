import React, { Component } from "react";

import {
  Navbar,
  NavbarToggler,
  NavbarBrand,
  Nav,
  NavItem,
  NavLink,
  NavbarText
} from 'reactstrap';
export class Header extends Component {
  render() {
    return (
      <Navbar color="light" light expand="md">
        <NavbarBrand href="/">Vaccine Locator</NavbarBrand>
        <Nav>
          <NavItem><NavLink href="/">Home</NavLink></NavItem>
          <NavItem><NavLink href="/">About us</NavLink></NavItem>
          <NavItem><NavLink href="/">Contact Us</NavLink></NavItem>
        </Nav>
      </Navbar>
    );
  }
}

export default Header;
