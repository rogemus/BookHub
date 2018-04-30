import React from 'react';
import PropTypes from 'prop-types';
import RegisterForm from '../registerForm/registerForm.component';

export default function UserDetails(props) {
	return (
		<div className='user-details'>
			<h1>User data</h1>

			<RegisterForm
				handleSubmit={props.handleSubmit}
				handleChange={props.handleChange}
				values=
					{{
						username: props.values.username,
						first_name: props.values.first_name,
						last_name: props.values.last_name,
						email: props.values.email
					}}
			/>
		</div>
	);
}

UserDetails.propTypes = {
	handleSubmit: PropTypes.func,
	handleChange: PropTypes.func,
	values: PropTypes.object
};
