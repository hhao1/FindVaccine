import { combineReducers } from "redux";
import leads from "./leads";
import vaccines from "./vaccines"
import markers from "./makers"

export default combineReducers({
  leadReducer: leads,
  vaccineReducer: vaccines,
  markerReducer: markers
});
