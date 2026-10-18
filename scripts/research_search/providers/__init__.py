"""Optional, offline-first multi-database provider adapters."""

from .base import Provider
from .fusion import fuse_results
from .fusion_export import export_provider_fusion
from .execution import ProviderTransport, execute_provider_plan, validate_provider_plan
from .models import FusionConflict, FusionResult, ProviderPaper, ProviderResult, SearchRequest
from .pubmed import PubMedProvider
from .semantic_scholar import SemanticScholarProvider

__all__ = [
    "Provider", "SearchRequest", "ProviderResult", "ProviderPaper",
    "FusionResult", "FusionConflict", "PubMedProvider", "SemanticScholarProvider",
    "fuse_results", "export_provider_fusion", "ProviderTransport", "execute_provider_plan", "validate_provider_plan",
]
