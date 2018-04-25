import {
	SET_CURRENT_USER,
	GET_CURRENT_USER
} from '../actions/types';

const INITIAL_STATE = {
	current: {},
	userData: {}
};

export default (state = INITIAL_STATE, action) => {
	switch (action.type) {
		case SET_CURRENT_USER:
			return {...state, current: action.payload};
		case GET_CURRENT_USER:
			return {...state, userData: action.payload};
	}

	return state;
};
