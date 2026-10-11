# Made with ❤️ by Vibey
"""
AWS concrete client adapter implementing the CloudClientPort protocol.

This file provides a minimal, declared‑only AWS implementation that satisfies the
``CloudClientPort`` interface. The methods raise ``NotImplementedError`` because the
real AWS adapter is declared only and should not perform any work until a full
implementation is added.

The adapter exists to make the contract suite pass in tests that import and
validate the interface implementation.
"""

from typing import Awaitable

from vibey.application.interfaces.azure import (
    CloudClientPort,
    AzureDiscoveryResult,
    AzureExecutionResult,
    AzureResourceStatus,
)
from vibey.domain.deployment import (
    AzureTargetScope,
    DeploymentConsent,
    DeploymentSpec,
)


class AwsClientAdapter(CloudClientPort):
    """A declared‑only AWS client that implements the CloudClientPort protocol.

    Each method simply raises ``NotImplementedError`` to indicate that the
    functionality has not yet been implemented.
    """

    async def discover_environment(self, scope: AzureTargetScope) -> AzureDiscoveryResult:  # type: ignore[override]
        raise NotImplementedError("AWS adapter not yet implemented")

    async def execute_plan(
        self, spec: DeploymentSpec, consent: DeploymentConsent
    ) -> AzureExecutionResult:  # type: ignore[override]
        raise NotImplementedError("AWS adapter not yet implemented")

    async def get_resource_status(
        self, scope: AzureTargetScope, resource_id: str
    ) -> AzureResourceStatus:  # type: ignore[override]
        raise NotImplementedError("AWS adapter not yet implemented")

    async def delete_resource(
        self, scope: AzureTargetScope, resource_id: str, consent: DeploymentConsent
    ) -> None:  # type: ignore[override]
        raise NotImplementedError("AWS adapter not yet implemented")
