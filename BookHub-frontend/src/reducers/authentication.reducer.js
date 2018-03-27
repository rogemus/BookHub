import {
	LOGIN
} from '../actions/types';

export default (state = {}, action) => {
	switch (action.type) {
		case LOGIN:
			return {...state, token: action.payload.token};
	}

	return state;
};
