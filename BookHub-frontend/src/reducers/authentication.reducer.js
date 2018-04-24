import {
	LOGIN,
	SET_TOKEN
} from '../actions/types';

const INITIAL_STATE = {
	token: '',
	isLogin: false
};

export default (state = INITIAL_STATE, action) => {
	switch (action.type) {
		case LOGIN:
			return {...state, isLogin: action.payload};
		case SET_TOKEN: {
			return {...state, token: action.payload};
		}
	}

	return state;
};
