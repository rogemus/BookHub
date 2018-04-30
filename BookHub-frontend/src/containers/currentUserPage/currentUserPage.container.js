import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import _isEmpty from 'lodash/isEmpty';
import { getCurrentUserData } from '../../actions/user.actions';
import UserDetails from '../../components/userDetails/userDetails.component';

class CurrentUserPage extends Component {
	constructor(props) {
		super(props);
		this.state = {
			first_name: '',
			last_name: '',
			email: '',
			password: '',
			username: ''
		};
	}

	componentDidMount() {
		document.title = 'BookHub | Me';

		this.props.getCurrentUserData(this.props.token);
	}

	onSubmit($event) {
		$event.preventDefault();
	}

	onChange($event) {
		this.setState({[$event.target.name]: $event.target.value});
	}

	renderUserDetails() {
		if (!_isEmpty(this.props.userData)) {
			return <UserDetails
				handleSubmit={this.onSubmit.bind(this)}
				handleChange={this.onChange.bind(this)}
				values={{
					username: this.props.userData.username,
					first_name: this.props.userData.first_name,
					last_name: this.props.userData.last_name,
					email: this.props.userData.email
				}}
			/>;
		}
	}

	render() {
		return (
			<div className='page-container'>
				{this.renderUserDetails()}
			</div>
		);
	}
}

function mapStateToProps(state) {
	return {
		userData: state.user.userData,
		token: state.authentication.token
	};
}

CurrentUserPage.propTypes = {
	token: PropTypes.string.isRequired,
	userData: PropTypes.object.isRequired,
	getCurrentUserData: PropTypes.func.isRequired
};

export default connect(mapStateToProps, {getCurrentUserData})(CurrentUserPage);

