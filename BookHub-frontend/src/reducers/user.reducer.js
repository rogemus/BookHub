import {
	SET_CURRENT_USER
} from '../actions/types';

const INITIAL_STATE = {
	current: {}
};

export default (state = INITIAL_STATE, action) => {
	switch (action.type) {
		case SET_CURRENT_USER:
			return {...state, current: action.payload};
	}

	return state;
};
