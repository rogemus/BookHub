import { _get } from './axios.actions';
import { GET_CURRENT_USER } from './types';

export function getCurrentUserData(token) {
	const config = {
		path: 'accounts/me',
		type: GET_CURRENT_USER,
		noApiUrl: true,
		conf: {
			headers: {
				'Authorization': `Bearer ${token}`
			}
		}
	};

	return _get(config.path, config.conf, config.type, config.noApiUrl);
}
