import { GET_LEADS } from "../actions/types.js";
import { func } from "prop-types";
const initialState = {
  leads: []
};
export default function(state = initialState, action) {
  switch (action.type) {
    case GET_LEADS:
      return {
        ...state,
        leads: action.payload
      };
    default:
      return state;
  }
}
