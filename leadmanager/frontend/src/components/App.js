import React, { Component } from "react";
import ReactDOM from "react-dom";
import Header from "./Layout/Header";
import Dropdown from "./Layout/Dropdown";

class App extends Component {
  render() {
    return (
      <div>
        <Header />
        <Dropdown />
      </div>
    );
  }
}
ReactDOM.render(<App />, document.getElementById("app"));
