import React from 'react';
import PropTypes from 'prop-types';
import { Table, Header } from 'semantic-ui-react';

export default function UserDetails({userData}) {
	return (
		<div>
			<Header as='h2' textAlign='center'>
				User data
			</Header>
			<Table basic='very' celled>
				<Table.Body>
					<Table.Row>
						<Table.Cell>
							<Header as='h4'>
								Username
							</Header>
						</Table.Cell>
						<Table.Cell>
							{userData.username}
						</Table.Cell>
					</Table.Row>
					<Table.Row>
						<Table.Cell>
							<Header as='h4'>
								Email
							</Header>
						</Table.Cell>
						<Table.Cell>
							{userData.email}
						</Table.Cell>
					</Table.Row>
					<Table.Row>
						<Table.Cell>
							<Header as='h4'>
								First Name
							</Header>
						</Table.Cell>
						<Table.Cell>
							{userData.first_name}
						</Table.Cell>
					</Table.Row>
					<Table.Row>
						<Table.Cell>
							<Header as='h4' image>
								Last Name
							</Header>
						</Table.Cell>
						<Table.Cell>
							{userData.last_name}
						</Table.Cell>
					</Table.Row>
				</Table.Body>
			</Table>
		</div>
	);
}

UserDetails.propTypes = {
	userData: PropTypes.object.isRequired
};
