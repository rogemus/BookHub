import {
	LOGIN
} from '../actions/types';

const INITIAL_STATE = {
	token: ''
};

export default (state = INITIAL_STATE, action) => {
	switch (action.type) {
		case LOGIN:
			return {...state, token: action.payload.token};
	}

	return state;
};
