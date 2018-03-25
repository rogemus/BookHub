import {
	GET_TOKEN
} from '../actions/types';

export default (state = {}, action) => {
	switch (action.type) {
		case GET_TOKEN:
			return {...state, token: action.payload.token};
	}

	return state;
};
