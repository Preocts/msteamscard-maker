from __future__ import annotations

import dataclasses

from cardmaker.model.base_element import BaseElement


@dataclasses.dataclass(repr=False)
class MediaSource:
    mimeType: str
    url: str


@dataclasses.dataclass(repr=False)
class Media(BaseElement):
    """
    Define a Media Card Element used inside `content.body[]`

    Single media sources can be defined in the construction of object while
    multiple media sources are added with `.add_source()`
    """

    type: str = "Media"
    sources: list[MediaSource] = dataclasses.field(default_factory=list)
    poster: str | None = None
    altText: str | None = None

    # TODO: Make this work with __init__ 02.03.2022
    @classmethod
    def basic_setup(
        cls,
        mime_type: str,
        media_url: str,
        poster_url: str | None = None,
        altText: str | None = None,
    ) -> Media:
        """Build Media object with basic setup"""
        newobj = cls()
        newobj.add_source(mime_type, media_url)
        newobj.poster = poster_url
        newobj.altText = altText
        return newobj

    def add_source(self, mime_type: str, url: str) -> None:
        """
        Define a source for a Media element

        Args:
            mime_type: Mime type associated media (e.g. `video/mp4`)
            url: URL to media
        """
        self.sources.append(MediaSource(mime_type, url))

    def set_poster(self, url: str) -> None:
        """URL of an image to display before playing"""
        self.poster = url

    def set_altText(self, text: str) -> None:
        """Alternate text describing the audio or video"""
        self.altText = text
