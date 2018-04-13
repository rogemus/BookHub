import React from 'react';
import PropTypes from 'prop-types';
import { Form, Button } from 'semantic-ui-react';

export default function RegisterForm(props) {
	return (
		<Form onSubmit={props.handleSubmit}>
			<Form.Field required>
				<label>Username</label>
				<input
					placeholder='Username'
					value={props.values.username}
					onChange={props.handleChange}
					name='username'
					type='text'
				/>
			</Form.Field>
			<Form.Field required>
				<label>Name</label>
				<input
					placeholder='First Name'
					value={props.values.first_name}
					onChange={props.handleChange}
					name='first_name'
					type='text'
				/>
			</Form.Field>
			<Form.Field required>
				<label>Surname</label>
				<input
					placeholder='Last Name'
					value={props.values.last_name}
					onChange={props.handleChange}
					name='last_name'
					type='text'
				/>
			</Form.Field>
			<Form.Field required>
				<label>Email</label>
				<input
					placeholder='Email'
					required
					value={props.values.email}
					onChange={props.handleChange}
					name='email'
					type='email'
				/>
			</Form.Field>
			<Form.Field required>
				<label>Password</label>
				<input
					placeholder='Password'
					required
					onChange={props.handleChange}
					value={props.values.password}
					name='password'
					type="password"
				/>
			</Form.Field>
			<Button type='submit' primary>Submit</Button>
		</Form>
	);
}

RegisterForm.propTypes = {
	handleSubmit: PropTypes.func,
	handleChange: PropTypes.func,
	values: PropTypes.object
};
