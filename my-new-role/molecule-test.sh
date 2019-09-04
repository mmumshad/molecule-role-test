
SECONDS=0
# Clean, Destroy and Test again. Do not destroy after test.

# docker exec -e TEST_DIRECTORY=tests/tests-3 molecule-tester molecule destroy --scenario-name playbook-1


# docker exec -e TEST_DIRECTORY=tests/tests-3 molecule-tester molecule test --scenario-name playbook-1 --destroy=never

docker exec -e TEST_DIRECTORY=tests/tests-4 molecule-tester molecule cleanup --scenario-name playbook-1
docker exec -e TEST_DIRECTORY=tests/tests-4 molecule-tester molecule converge --scenario-name playbook-1
docker exec -e TEST_DIRECTORY=tests/tests-4 molecule-tester molecule verify --scenario-name playbook-1

duration=$SECONDS
echo "$(($duration / 60)) minutes and $(($duration % 60)) seconds."
