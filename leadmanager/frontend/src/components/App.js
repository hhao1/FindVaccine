import React, { Component } from "react";
import ReactDOM from "react-dom";
import Header from "./Layout/Header";
import Dropdown from "./Layout/Dropdown";
import { Provider } from "react-redux";
import store from "../store";

class App extends Component {
  render() {
    return (
      <Provider store={store}>
        <Header />
        <Dropdown />
      </Provider>
    );
  }
}
ReactDOM.render(<App />, document.getElementById("app"));
