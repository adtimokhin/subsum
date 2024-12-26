"use client";

import {
  Box,
  Heading,
  SimpleGrid,
  Button,
  VStack,
  Text,
  Table,
} from "@chakra-ui/react";

export default function Dashboard() {
  const userName = "Aleksandr Timokhin"; // Replace with dynamic user data

  const upcomingPayments = [
    { name: "Netflix", daysUntil: 3, amount: "$15.99" },
    { name: "Spotify", daysUntil: 7, amount: "$9.99" },
    { name: "Amazon Prime", daysUntil: 14, amount: "$12.99" },
  ];

  return (
    <VStack align="stretch" p={8}>
      {/* Welcome Message */}
      <Box textAlign="left">
        <Heading as="h1" size="2xl" mb={4}>
          Welcome, {userName}!
        </Heading>
      </Box>

      {/* Bento Grid */}
      <SimpleGrid columns={{ base: 1, md: 1 }}>
        {/* Rectangle 1: Upcoming Payments */}
        <SimpleGrid columns={{ base: 1, md: 2 }}>
          <Box bg="gray.200" borderRadius="md" boxShadow="md" p={4}>
            <Heading as="h2" size="md" mb={4} textAlign="center">
              Upcoming Payments
            </Heading>
            <Table.Root>
              <Table.Header>
                <Table.Row>
                  <Table.ColumnHeader textAlign="start">
                    Subscription
                  </Table.ColumnHeader>
                  <Table.ColumnHeader textAlign="start">
                    Due in
                  </Table.ColumnHeader>
                  <Table.ColumnHeader textAlign="end">Price</Table.ColumnHeader>
                </Table.Row>
              </Table.Header>
              <Table.Body>
                {upcomingPayments.map((item) => (
                  <Table.Row key={item.name}>
                    <Table.Cell>{item.name}</Table.Cell>
                    <Table.Cell>{item.daysUntil}</Table.Cell>
                    <Table.Cell textAlign="end">{item.amount}</Table.Cell>
                  </Table.Row>
                ))}
              </Table.Body>
            </Table.Root>
          </Box>

          <Box
            bg="teal.400"
            height="100px"
            borderRadius="md"
            boxShadow="md"
            textAlign="center"
            display="flex"
            alignItems="center"
            justifyContent="center"
            color="white"
          >
            <Button
              colorScheme="teal"
              size="lg"
              onClick={() => {
                console.log("Add subscription button clicked");
              }}
            >
              Add New Subscription
            </Button>
          </Box>
        </SimpleGrid>

        <Box
          bg="teal.300"
          height="100px"
          borderRadius="md"
          boxShadow="md"
          textAlign="center"
          display="flex"
          alignItems="center"
          justifyContent="center"
          color="white"
        >
          <Text>Rectangle 3</Text>
        </Box>
      </SimpleGrid>

      {/* Large Add Subscription Button */}
      <Box textAlign="center" mt={10}>
        <Button
          colorScheme="teal"
          size="lg"
          onClick={() => {
            console.log("Add subscription button clicked");
          }}
        >
          Update Subscription
        </Button>
      </Box>
    </VStack>
  );
}
